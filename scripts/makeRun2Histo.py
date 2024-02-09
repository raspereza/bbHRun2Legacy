import ROOT as r
import argparse

# Define the allowed values for CHANNEL, CATEGORY, and MODE
VALID_CHANNELS = ["em", "et", "mt", "tt"]
VALID_CATEGORIES = ["1", "2", "3", "4"]
VALID_YEARS = ["2016", "2017", "2018"]
VALID_MODES = ["prefit", "postfit"]

def main():
    parser = argparse.ArgumentParser(description="Process a ROOT file.")
    parser.add_argument("input_file", help="Path to the input ROOT file")
    parser.add_argument("--channel", help="Channel")
    parser.add_argument("--category", help="Category")
    parser.add_argument("--mode", help="Prefit or postfit")
    args = parser.parse_args()
    print(args.input_file)
    channel=args.channel
    category=args.category
    mode=args.mode
    # Open the input ROOT file in update mode
    input_file = r.TFile.Open(args.input_file,"UPDATE")

    # Loop through the combination of CHANNEL, CATEGORY, and MODE
    # Build the output directory name
    output_directory_name = "bbhtt_"+channel+"_"+category+"_13TeVRun2_"+mode
    output_directory = input_file.mkdir(output_directory_name)

    # Create a dictionary to store the summed histograms
    summed_histograms = {}

    # Loop through the YEAR variable
    for year in VALID_YEARS:
        # Build the input directory name
        directory_name = "bbhtt_"+channel+"_"+category+"_13TeV"+year+"_"+mode

        # Check if the directory exists in the input file
        if input_file.Get(directory_name):
            print("Found directory: "+directory_name)
            input_directory = input_file.Get(directory_name)

            # Loop through histograms in the input directory
            for key in input_directory.GetListOfKeys():
                # Get the histogram name
                hist_name = key.GetName()
                
                # Get the histogram from the input directory
                hist = input_directory.Get(hist_name)

                # Sum histograms with the same name from different years
                if hist_name not in summed_histograms:
                    summed_histograms[hist_name] = hist.Clone()
                else:
                    for iBin in range(1, hist.GetNbinsX()+1 ):
                        summed_histograms[hist_name].Fill(hist.GetBinCenter(iBin), hist.GetBinContent(iBin))

                        
    # Store the summed histograms in the output directory
    for hist_name, summed_hist in summed_histograms.items():
        output_directory.cd()
        output_directory.WriteObject(summed_histograms[hist_name], hist_name)

    # Close the input file to save changes
    input_file.Close()

if __name__ == "__main__":
    main()
