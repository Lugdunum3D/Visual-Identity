SRC = logos.svg
IDS = epitech vulkan gltf2
SVG = $(IDS:%=dist/%.svg)
PNG = $(IDS:%=dist/%.png)

all: $(SVG) $(PNG)

$(SVG): $(SRC)
	@echo building $@ $(dir $@) $(basename $(notdir $@))
	mkdir -p $(dir $@)
	python ./exportlayers.py $(basename $(notdir $@)) $(SRC) $@
	inkscape --verb=FitCanvasToDrawing --verb=FileSave --verb=FileQuit $@

dist/%.png: dist/%.svg
	@echo building $@ in $(dir $@) from $^
	mkdir -p $(dir $@)
	inkscape --file=$^ --export-png=$@ --export-dpi=384

clean:
	rm -r dist $(LOGO)

.PHONY: clean
