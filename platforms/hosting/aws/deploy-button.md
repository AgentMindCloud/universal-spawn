# AWS — Deploy-button recipe

A manifest that declares `platforms.aws` with a
complete `samconfig.toml / cdk.json`-equivalent block is eligible
for the canonical AWS Deploy button. Drop this snippet
into the repository's `README.md` to surface it.

## Markdown

```markdown
[![Launch on AWS](https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=your-stack&templateURL=https%3A%2F%2Fs3.amazonaws.com%2Fyour-bucket%2Ftemplate.yaml)
```

## HTML

```html
<a href="https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=your-stack&templateURL=https%3A%2F%2Fs3.amazonaws.com%2Fyour-bucket%2Ftemplate.yaml">
  <img src="https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png" alt="Launch Stack" />
</a>
```

## Parameters

The CloudFormation launch URL accepts:

- `region` — AWS region for the stack.
- `stackName` — default stack name.
- `templateURL` — URL-encoded URL of the template file (usually an S3 URL).

Generators SHOULD fill `region` from `platforms.aws.region` and upload the generated template before rendering the button.

## Badge style

The universal-spawn project ships a complementary "Spawns on
AWS" badge you can pair with the Deploy button. The badge
verifies against the platform schema at install time; a manifest that
fails `aws-spawn.schema.json` loses the badge.

```markdown
[![Spawns on AWS](https://universal-spawn.dev/badge/aws.svg)](https://universal-spawn.dev/registry/aws)
```
