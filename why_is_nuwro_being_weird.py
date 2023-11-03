import ROOT
from ROOT import gStyle, TCanvas, TH1D, TLegend, kRed, kBlue


#generator_rootfile = "T2KND_FHC_numu_C8H8_NUWRO_LFGRPA_1M_0000_NUISFLAT.root"
generator_rootfile  = " T2KND_FHC_numu_C8H8_NEUT562_1M_0000_NUISFLAT.root"
particle = 2112

datafile = ROOT.TFile.Open(generator_rootfile, "read")
Tree = datafile.Get('FlatTree_VARS')

histo1 = ROOT.TH1F("hist", " {} Particle Energy vs Transparency".format(particle), 500,0.938,3)
histo2 = ROOT.TH1F("hist", " {} Particle Energy vs Transparency".format(particle), 500,0.938,3)
#this histo is copied at the end and its copy is returned, so its named now cuz i dunno how else
#to name it later.
count = 0
eventcount = 0  
for event in Tree:
    found_init = False # is the particle found before the vertex?
    found_vert = False # is the particle found at the vertex?
    found_fs = False # is the particle found after the vertex?
    E_vert = 0 # vertex energy
    E_fs = 0 # final state energy. is a list cuz for each event there could be many final state e.g. protons


    if(len(event.pdg) == 2): #ignores all two particle final state events.
        continue

    for i in range (0,len(event.pdg_init)): # loops over initial state particles to find desired particle
        if (event.pdg_init[i] == particle):
            found_init = True
            continue

    for i in range (0,len(event.pdg_vert)): # loops over vertex particles to find desired particle
        if (event.pdg_vert[i] == particle):
            found_vert = True
            E_vert = event.E_vert[i] #stores particles vertex energy
            for j in range (0, len(event.pdg)): #does same as above for final state, adds all desired particles energies to list
                if(event.pdg[j] == particle and abs(event.E[j] - E_vert) < 0.0001):
                    found_fs = True
                    print("final energy {}".format(event.E[j]))
                    print("early energy {}".format(E_vert))

                    eventcount += 1 

                    continue

    if count == 100000: #kills loop at number of counts
        break
    count += 1  


print(eventcount/count)

"""

    if(found_vert): 
    #selects events where the particle is not a initial particle, but is in final state and the vertex 
        
        #plots all fs energies on histo 1
        histo2.Fill(E_vert) #plots vertex energies on histo 2

    if(found_vert and found_fs):
        histo1.Fill(E_vert)
    
    if count == 50000: #kills loop at number of counts
        break
    count += 1  

histo2.SetLineColor(kRed)    

canv = ROOT.TCanvas("newcanvas","New canvas",1000,800)
histo2.Draw()
histo1.Draw("same")

canv.Draw()

while True:
    user_input = input("Press Enter to exit: ")
    if user_input == "":
        break

"""


