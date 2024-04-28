import glob

target_directory = "Data/"

markdowns = glob.glob(target_directory + "**/*.md", recursive=True)
with open("combined_markdown.md", "w") as outfile:
    for filename in markdowns:
        with open(filename) as infile:
            outfile.write("## This section comes from " + filename + "\n")
            outfile.write(infile.read())
            # write a line about the filepath
            outfile.write("\n\n")