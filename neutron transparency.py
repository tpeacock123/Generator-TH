import ROOT
from ROOT import kRed


                    
datafile = ROOT.TFile.Open(" T2KND_FHC_numu_C8H8_NEUT562_1M_0000_NUISFLAT.root", "read")
Tree = datafile.Get('FlatTree_VARS')

histo1 = ROOT.TH1F("hist", "hist", 1000,0,2)
histo2 = ROOT.TH1F("hist", "hist", 1000,0,2)
histo4 = ROOT.TH1F("hist", "hist", 1000,0,2)
histo2.SetLineColor(kRed)


count = 0
for event in Tree:
    found_init = False
    proton_found = False
    proton_found_fs = False
    proton_E = 0
    proton_E_fs = 0


    if(len(event.pdg) == 2):
        continue
    
    for i in range (0,len(event.pdg_init)):
        if (event.pdg_init[i] == 2112):
            proton_found_init = True
            
    for i in range (0,len(event.pdg_vert)):
        if (event.pdg_vert[i] == 2212):
            proton_found = True
            proton_E = event.E_vert[i]
            
    for i in range (0, len(event.pdg)):
        if (event.pdg[i] != 2212):
            proton_found_fs = True
            proton_E_fs = event.E[i]

    
    if((found_init) and proton_found_fs and proton_found):
        histo1.Fill(proton_E_fs)
        histo2.Fill(proton_E)

        
        histo4.Fill(proton_E_fs/proton_E)
    
    if count == 100000:
        break
    count += 1  

h3 = histo1.Clone("h3")
h3.Divide(histo2)

canv = ROOT.TCanvas("newcanvas","New canvas",800,600)
h3.Draw()
#histo4.Draw( 
canv.Draw()

while True:
    user_input = input("Press Enter to exit: ")
    if user_input == "":
        break
