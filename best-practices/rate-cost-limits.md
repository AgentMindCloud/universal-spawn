# Rate limits and cost ceilings

`safety.rate_limit_qps` and `safety.cost_limit_usd_daily` are the
two numerical knobs that let a manifest declare "I will not spend
more than this." They're advisory by spec but enforced as hard
ceilings by every conformant platform. Treat them like seatbelts:
boring until they save you.

## What each one means

- **`rate_limit_qps`** — sustained outbound queries per second the
  creation will produce. Burst is fine; sustained excess is not.
- **`cost_limit_usd_daily`** — hard daily ceiling on the total USD
  cost the creation can incur. Spawning halts before this cap is
  exceeded.

Both numbers cover *aggregate* traffic across all calls a single
spawn makes. They are not per-tool or per-route.

## Suggested numbers by use case

These are starting points, not commandments.

| Creation kind | rate_limit_qps | cost_limit_usd_daily |
|---|---|---|
| Personal Discord bot, hobby | 1 | 2 |
| X reply bot, single account | 3–5 | 10–20 |
| Customer-support agent | 10 | 50 |
| Internal research agent | 3 | 30 |
| Background data pipeline | 1–2 | 5 |
| Public Web App, low-traffic | 50 | 25 |
| Production API service | 100+ | based on infra plan |
| GPU inference endpoint | 5 | 50–200 |

Rule of thumb: pick the daily cost cap such that "the bot ran
unattended for a week" is recoverable, not catastrophic. A weekend
mistake should cost a coffee, not a mortgage payment.

## How to estimate your numbers

1. Run the creation against real-ish input for an hour.
2. Note (a) requests per second and (b) USD spent.
3. Multiply each by 24× and add a 2× buffer. That's your starting
   `cost_limit_usd_daily`.
4. Use the higher of (your peak qps × 1.5) or (your QPS quota at
   the upstream API) as `rate_limit_qps`.

## What happens at the ceiling

Conformant platforms implement these as *hard* ceilings:

- When `cost_limit_usd_daily` is reached, the platform halts further
  spawns that key the same accounting bucket. It does NOT let the
  creation finish "the current call" — the cap is the cap.
- When `rate_limit_qps` is exceeded, requests get queued or rejected
  per the platform's standard behavior (HTTP 429, Discord rate-limit
  bucket, etc.). The platform does NOT silently drop them.

Most platforms also implement a "soft warning" threshold at 80% of
each cap. Use that as a feature, not as a substitute for the hard
ceiling.

## Patterns

### "Throttle me hard during peak hours"

The spec doesn't include time-of-day rate scheduling. If you need
it, declare a conservative `rate_limit_qps` and let your platform's
own scheduler shape traffic.

### "I have variable cost per call"

Pick the limit assuming worst-case (Opus, max thinking budget, max
tools) — not average. The cap exists for the bad day, not the
median day.

### "I really do want to allow $500/day"

Be loud about it in `description`. Pair with `safe_for_auto_spawn:
false` and a clear runbook in your README. Reviewers correctly
flag any `cost_limit_usd_daily` over $100 as worth a second look.

### "I run on a flat-fee infrastructure"

Set `cost_limit_usd_daily: 0`. The cap still exists; it just
declares "this creation does not incur per-call cost." Useful for
self-hosted deployments where the only cost is the underlying
servers.

## Common mistakes

- Setting the cap based on what you wish you spent, not what you
  actually spend. Capping a $30/day bot at $5 just causes mysterious
  3pm outages.
- Forgetting that `cost_limit_usd_daily` is per *spawn account* in
  most platforms, not per manifest. A team of ten running the same
  manifest can spend ten times the cap before anyone notices.
- Leaving `rate_limit_qps` unset on an LLM-tool agent. A single
  badly-prompted loop can turn a $5/hour bot into a $500/hour bill
  in two minutes.

## Tying it back to the safety envelope

`rate_limit_qps`, `cost_limit_usd_daily`, `min_permissions`, and
`safe_for_auto_spawn` form a system. None of the four is sufficient
on its own, but together they give the platform enough to enforce a
declared blast radius. Treat them as four required disciplines for
any production manifest, not as four optional fields.
