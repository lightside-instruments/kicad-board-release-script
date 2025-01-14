kicad-cli version | tee kicad-version.txt
kicad-cli version --format about | tee kicad-version-about.txt
kicad-cli sch export pdf --output=schematics.pdf ../*.kicad_sch
kicad-cli sch erc --output=erc.log ../*.kicad_sch
rm -rf gerbers
mkdir gerbers
kicad-cli pcb export gerbers --output=gerbers ../*.kicad_pcb
zip gerbers.zip gerbers/
kicad-cli pcb export vrml --output=model3d.wrl ../*.kicad_pcb
kicad-cli pcb export step --output=model3d.step ../*.kicad_pcb
