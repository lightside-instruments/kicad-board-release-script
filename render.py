import pcbnew 
filename = "../ice4pi.kicad_pcb" 
output_dir = "output/"    
board = pcbnew.LoadBoard(filename)    


plot_controller = pcbnew.PLOT_CONTROLLER(board)
plot_options = plot_controller.GetPlotOptions()    

pcb_bounding_box = board.ComputeBoundingBox() 
print("origin", pcb_bounding_box.GetOrigin()) 
print("height", pcb_bounding_box.GetHeight()) 
print("width", pcb_bounding_box.GetWidth())

plot_options.SetUseAuxOrigin(True) 
board.GetDesignSettings().SetAuxOrigin(pcb_bounding_box.GetOrigin())

currpageInfo = board.GetPageSettings()
currpageInfo.SetWidthMils(int(pcb_bounding_box.GetWidth() / pcbnew.IU_PER_MILS))
currpageInfo.SetHeightMils(int(pcb_bounding_box.GetHeight() / pcbnew.IU_PER_MILS))
board.SetPageSettings(currpageInfo) 

#python IU_PER_MM = pcbnew.IU_PER_MILS / 2.54 * 1000 VIEW_BOX_DIVIDER = 100  # Why that value? Wish I knew

new_svg_attributes = {    
    "width": f"{round(pcb_bounding_box.GetWidth() / IU_PER_MM, 5)}cm",   
    "height": f"{round(pcb_bounding_box.GetHeight() / IU_PER_MM, 5)}cm",   
    "viewBox": f"0 0 {int(pcb_bounding_box.GetWidth() / VIEW_BOX_DIVIDER)} {int(pcb_bounding_box.GetHeight() / VIEW_BOX_DIVIDER)}",  
}

settings_manager = pcbnew.GetSettingsManager() 
color_settings = settings_manager.GetColorSettings() 
plot_options.SetColorSettings(color_settings) 

top_layer = top_layer\
 .replace(KICAD_THEME_SEARCH["top_silkscreen"].encode("utf8"), theme["top_silkscreen"].encode("utf8"))\
 .replace(KICAD_THEME_SEARCH["top_mask"].encode("utf8"), theme["top_layer"].encode("utf8"))\
 .replace(KICAD_THEME_SEARCH["top_layer"].encode("utf8"), theme["top_mask"].encode("utf8"))\
 .replace(KICAD_THEME_SEARCH["edge_cuts"].encode("utf8"), theme["edge_cuts"].encode("utf8"))\
 .replace(KICAD_THEME_SEARCH["drill"].encode("utf8"), theme["drill"].encode("utf8"))

bottom_layer = bottom_layer\
 .replace(KICAD_THEME_SEARCH["bottom_silkscreen"].encode("utf8"), theme["bottom_silkscreen"].encode("utf8"))\
 .replace(KICAD_THEME_SEARCH["bottom_mask"].encode("utf8"), theme["bottom_layer"].encode("utf8"))\
 .replace(KICAD_THEME_SEARCH["bottom_layer"].encode("utf8"), theme["bottom_mask"].encode("utf8"))\
 .replace(KICAD_THEME_SEARCH["edge_cuts"].encode("utf8"), theme["edge_cuts"].encode("utf8"))\
 .replace(KICAD_THEME_SEARCH["drill"].encode("utf8"), theme["drill"].encode("utf8"))

plot_options.SetOutputDirectory(output_dir)
plot_options.SetPlotFrameRef(False)
#plot_options.SetDrillMarksType(pcbnew.PCB_PLOT_PARAMS.FULL_DRILL_SHAPE)
plot_options.SetSkipPlotNPTH_Pads(False)
plot_options.SetMirror(False)
plot_options.SetFormat(pcbnew.PLOT_FORMAT_SVG)
#plot_options.SetSvgPrecision(4, False)
plot_options.SetPlotViaOnMaskLayer(True)    
plot_controller.OpenPlotfile("mask", pcbnew.PLOT_FORMAT_SVG, "Top mask layer")
plot_controller.SetColorMode(True)
plot_controller.SetLayer(pcbnew.F_Mask)
plot_controller.PlotLayer()
plot_controller.ClosePlot() 
