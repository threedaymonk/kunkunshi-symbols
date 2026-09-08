SYMBOLS = $(shell find src/ -name '*.svg' -type f)
PDFS = \
	$(patsubst src/%.svg, build/%.pdf, \
	$(shell find src/ -name '*.svg' -type f))

.PHONY : all clean

all : build/kunkunshi-all.svg $(PDFS)

clean :
	git clean -fdx build

build/kunkunshi-all.svg : $(SYMBOLS)
	python xmlcombine.py $^ > $@

build/%.pdf : src/%.svg
	inkscape --export-filename="$@" "$<"
