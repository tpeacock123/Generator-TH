import ROOT
from ROOT import gStyle, TCanvas, TH1D, TLegend, kRed, kBlue

from transparencyHistoFunction import *

def main():
    """
    generatorTransparencyComparison
    - uses THF to generate a comparison plot of two  
    """
    ROOT.gStyle.SetOptStat(0) #removes auto legend, from here its pretty standard plotting

    Generator_rootfile1 = " T2KND_FHC_numu_C8H8_NEUT562_1M_0000_NUISFLAT.root"
    Generator_rootfile2 =  "T2KND_FHC_numu_C8H8_NUWRO_LFGRPA_1M_0000_NUISFLAT.root"
    events = 1000000
    particle = 211

    histoNUWRO = transparency_Histo(Generator_rootfile2,particle,events)
    histoNEUT = transparency_Histo(Generator_rootfile1,particle,events)
  
    histoNUWRO.SetLineColor(kRed)

    canv = ROOT.TCanvas("newcanvas","New canvas",1000,800)
    NEUT_max = float(histoNEUT.GetMaximumBin())
    NUWRO_max = float(histoNUWRO.GetMaximumBin())

    legend = TLegend(0.15, 0.75, 0.33, 0.88)
    legend.AddEntry(histoNUWRO, "NUWRO", "l")
    legend.AddEntry(histoNEUT, "NEUT", "l")
    legend.SetBorderSize(0)


    histoNEUT.GetXaxis().SetTitle("Kinetic Energy(GeV)")
    histoNEUT.GetYaxis().SetTitle("Transparency")
    histoNEUT.Draw()
    histoNUWRO.Draw("same")
   
    

    legend.Draw()
    canv.Draw()

    while True:
            user_input = input("Press Enter to exit: ")
            if user_input == "":
                break

    del histoNEUT
    del histoNUWRO


if __name__ == "__main__":
    main()
