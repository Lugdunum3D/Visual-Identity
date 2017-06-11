SRC = logo.svg
IDS = long short short-shadowed short-dark long-dark lugbench-long lugbench-short lugbench-short-shadowed lugbench-short-dark lugbench-long-dark
SVG = $(IDS:%=dist/%.svg)
PDF = $(IDS:%=dist/pdf/%.pdf)
DPI = 96 300 600
PNG = $(foreach dpidir, $(foreach dpi,$(DPI),dist/png/$(dpi)dpi/), $(IDS:%=$(dpidir)%.png))
LOGO = logo.png

all: $(SVG) $(PNG) $(PDF) $(LOGO)

$(SVG): $(SRC)
	@echo building $@ $(dir $@) $(basename $(notdir $@))
	mkdir -p $(dir $@)
	python ./exportlayers.py $(basename $(notdir $@)) $(SRC) $@
	inkscape --verb=FitCanvasToDrawing --verb=FileSave --verb=FileQuit $@

dist/png/96dpi/%.png: dist/%.svg
	@echo building $@ in $(dir $@) from $^
	mkdir -p $(dir $@)
	inkscape --file=$^ --export-png=$@ --export-dpi=96

dist/png/300dpi/%.png: dist/%.svg
	@echo building $@ in $(dir $@) from $^
	mkdir -p $(dir $@)
	inkscape --file=$^ --export-png=$@ --export-dpi=300

dist/png/600dpi/%.png: dist/%.svg
	@echo building $@ in $(dir $@) from $^
	mkdir -p $(dir $@)
	inkscape --file=$^ --export-png=$@ --export-dpi=600

dist/pdf/%.pdf: dist/%.svg
	@echo building $@ in $(dir $@) from $^
	mkdir -p $(dir $@)
	inkscape --file=$^ --export-pdf=$@ --export-dpi=300

$(LOGO): $(SRC)
	@echo building $@ in $(dir $@) from $^
	inkscape --file=$^ --export-png=$@ --export-dpi=300

clean:
	rm -r dist $(LOGO)

.PHONY: clean
