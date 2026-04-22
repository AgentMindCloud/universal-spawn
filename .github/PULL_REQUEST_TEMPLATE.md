<!--
  Thanks for contributing to universal-spawn.
  Please fill in every applicable section. Unchecked items block merge.
-->

## Summary

One paragraph — what this PR changes and why.

## Kind

- [ ] Spec change (prose + schema + matrix + example + CHANGELOG)
- [ ] New platform folder
- [ ] Example addition
- [ ] Documentation
- [ ] Editorial (typo / wording / link fix)

## Checklist

- [ ] Prose in `spec/vX.Y.Z/spec.md` updated (for spec changes)
- [ ] Schema in `spec/vX.Y.Z/manifest.schema.json` updated (for spec changes)
- [ ] Field reference `spec/vX.Y.Z/fields.md` updated
- [ ] Compatibility matrix `spec/vX.Y.Z/compatibility-matrix.md` updated
- [ ] At least one example in `examples/` demonstrates the change
- [ ] `CHANGELOG.md` entry added
- [ ] All examples still validate (`ajv validate -s ... -d ...`)
- [ ] No emoji anywhere (README, docs, schemas, comments)

## Related issues

Closes #

## Notes for reviewers

Anything that is easy to miss: subtle compatibility matrix changes,
reasons you chose one schema shape over another, platform-specific
quirks.
