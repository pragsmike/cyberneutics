.PHONY: pack

OUTPUT_FILE := $(HOME)/cyberneutics-pack.txt
INCLUDE_PATTERNS := *.md *.txt Makefile

# Construct find arguments: -name "pat1" -o -name "pat2" ...
# note: we use 'subst' and 'foreach' to avoid shell/sed dependency for string manipulation if possible,
# but 'sed' is often robust. Let's strictly follow the plan to use shell/sed as it handles spaces well in simple cases.
# Actually, Make's 'subst' is safer regarding shell glob expansion.
# Let's try a pure Make approach for stability.
# replace space with ' -o -name '
SPACE := $(subst ,, )
FIND_ARGS := -name "$(firstword $(INCLUDE_PATTERNS))"
FIND_ARGS += $(foreach p,$(wordlist 2,$(words $(INCLUDE_PATTERNS)),$(INCLUDE_PATTERNS)),-o -name "$(p)")

pack:
	@echo "Creating $(OUTPUT_FILE)..."
	@echo "Including patterns: $(INCLUDE_PATTERNS)"
	@find . -type f \( $(FIND_ARGS) \) ! -path "*/.*" ! -path "*/node_modules/*" | sort | while read -r file; do \
		echo "========== FILE: $$file =========="; \
		cat "$$file"; \
		echo ""; \
		echo "========== END FILE =========="; \
		echo ""; \
	done > $(OUTPUT_FILE)
	@echo "" >> $(OUTPUT_FILE)
	@echo "========== DIRECTORY LISTING: ls -lR ===========" >> $(OUTPUT_FILE)
	@ls -lR >> $(OUTPUT_FILE)
	@echo "" >> $(OUTPUT_FILE)
	@echo "========== END DIRECTORY LISTING ===========" >> $(OUTPUT_FILE)
	@echo "Done! Created $(OUTPUT_FILE)"
