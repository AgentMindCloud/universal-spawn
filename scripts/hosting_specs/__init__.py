"""Per-provider SPEC modules for platforms/hosting/.

Mirrors scripts/ai_specs/ but targets hosting / cloud destinations.
Each module exposes:

    SPEC: dict[str, Any]

consumed by scripts/gen_hosting_platform.generate().

Layout:

  vercel.py, netlify.py, railway.py, fly_io.py, render.py,
  cloudflare.py, heroku.py, aws.py, gcp.py, azure.py,
  digitalocean.py, supabase.py, firebase.py, deno_deploy.py,
  koyeb.py, northflank.py, pythonanywhere.py, hetzner.py,
  linode.py, vultr.py
"""
