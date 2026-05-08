.PHONY: signoff

signoff:
	@test -n "$(MSG)" || (echo "Usage: make signoff MSG='commit message'"; exit 1)
	@TAG="$$(python3 scripts/next_tag.py)"; \
	echo "Using tag: $$TAG"; \
	git add -A; \
	git commit -s -m "$(MSG)"; \
	git tag -a "$$TAG" -m "$$TAG"; \
	git push; \
	git push --tags
