.PHONY: signoff fmt clean

signoff:
	@test -n "$(MSG)" || (echo "Usage: make signoff MSG='commit message'"; exit 1)
	@TAG="$$(python3 scripts/next_tag.py)"; \
	echo "Using tag: $$TAG"; \
	git add -A; \
	git commit -S -s -m "$(MSG)"; \
	git tag -s -a "$$TAG" -m "$$TAG"; \
	git push; \
	git push --tags

fmt:
	find . -type f -name '*.tex' -print0 | xargs -0 latexindent -w
	find . -type f -name '*.bak*' -delete
	find . -type f -name 'indent.log' -delete

clean:
	rm -f *.bak* *.aux *.fdb_latexmk *.fls *.log *.out *.synctex.gz
	find . -type f -name '*.bak*' -delete
	find . -type f -name 'indent.log' -delete
