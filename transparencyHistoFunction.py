import ROOT
from ROOT import gStyle, TCanvas, TH1D, TLegend, kRed, kBlue


def transparency_Histo(generator_rootfile, particle, events):
    
    """
    ~~~~~~~~~~~~~ Transparency_Histo ~~~~~~~~~~~~~~~~~

    This function utilises PyRoot methods to produce a 
    transparency histogram for a given generator file 
    and particle (given as a pdg code)

    inputs
    - a t2k event generator root file containing a TTree
      called FlatTree_VARS 
    - the pdg code for a desired particle 
    - the number of events desired for loop
    
    output 
    - a root TH1F histogram of the particles fsi energy
      histo and vertex energy histo divided. 
    
    """

    datafile = ROOT.TFile.Open(generator_rootfile, "read")
    Tree = datafile.Get('FlatTree_VARS')

    histo1 = ROOT.TH1F("hist", " {} Particle Energy vs Transparency".format(particle), 400,0.13,1.135)
    histo2 = ROOT.TH1F("hist", " {} Particle Energy vs Transparency".format(particle), 400,0.13,1.135)
    #this histo is copied at the end and its copy is returned, so its named now cuz i dunno how else
    #to name it later.
    count = 0
    for event in Tree:
        found_init = False # is the particle found before the vertex?
        found_vert = False # is the particle found at the vertex?
        found_fs = False # is the particle found after the vertex?
        E_vert = 0 # vertex energy
        E_fs = 0 # final state energy. is a list cuz for each event there could be many final state e.g. protons


        #if(len(event.pdg) == 2): #ignores all two particle final state events.
        #    continue

        for i in range (0,len(event.pdg_init)): # loops over initial state particles to find desired particle
            if (event.pdg_init[i] == particle):
                found_init = True

                
        
                
        for i in range (0,len(event.pdg_vert)): # loops over vertex particles to find desired particle
            if (event.pdg_vert[i] == particle and found_init == False):
                found_vert = True
                E_vert = event.E_vert[i] #stores particles vertex energy
                for j in range (0, len(event.pdg)): #does same as above for final state, adds all desired particles energies to list
                    if(event.pdg[j] == particle and abs(event.E[j] - E_vert) < 0.00000001):
                        found_fs = True
                        continue

        
        if(found_vert): 
        #selects events where the particle is not a initial particle, but is in final state and the vertex 
           
            #plots all fs energies on histo 1
            histo2.Fill(E_vert) #plots vertex energies on histo 2

        if(found_vert and found_fs):
            histo1.Fill(E_vert)
        
        if count == events: #kills loop at number of counts
            break
        count += 1  

    h3 = histo1.Clone("h3") #clones histo 2 to perform operations on and to keep memory not messy (i think)
    h3.Divide(histo2) # divide h1/h2

    
    h3.SetDirectory(0) #unconnects h3 to the genny source file so it is returned. have to manually remove this tho
    return h3
    del h1
    del h2
    






