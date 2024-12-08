# Mains Hum and Audio Comparison
## Intro
This project is intended to be a forensic investigation tool. It enables extraction of key frequency ranges from audio samples. The background signals can be used to compare multiple different sources or audio files and determine if they were recorded at the same place or at the same time.
<br/><br/>
The electrical grid in the US runs at 60Hz with very little deviation. Historical data of the exact signal produced along the grid can be accessed by investigators. By extracting a narrow frequency band around 60Hz in audio recordings taken as evidence, it is theorietically possible to compare the ~60Hz component of the audio evidence to historical readings of the grid to determine an exact time when a file was recorded. This information is extremely valuable in instances where metadata for a file was overwritten or otherwise modified.
<br/>
<br/>
For more information on how this project works, see the detailed write up at [INSERT LINK TO PAPER HERE].
## CLI
This project comes with a cli, which is the primary way of interfacing with it. There are two tasks that can be accomplished through the cli, explained below.
### Extraction
Real world invesitagtions focusing on comparing evidence against the mains hum would not need this mode, but in cases where an invesitgator does not have access to historical mains data or would like to compare audio evidence on different frequency ranges, this mode is useful.
<br/>
This mode takes one sample file and extracts a given range of frequencies from it, writing the extracted data into a new .wav file.
#### Usage
`python cli.py x [sample file] [frequency] [range] [output file]`
<br/>
- x: Specifies extract mode. Can also be written as `extract`. <br/>
- sample file: Takes a relative path for the file from which data should be extracted. Can be any file that contains audio data. <br/>
- frequency: The core frequency in Hz that should be extracted from the sample.
- range: How many Hz in either direction from the core frequency should be accepted through the filter. This is not an exact measure due to how the filtering method works.
- output file: Where the extracted signal should be saved to. Should end in `.wav`.
#### Output
After running extract, a new file will be created which contains only the desired frequencies from the input signal.
### Comparison
This is the primary mode of operation of the tool. Compare mode takes two files, one being an unedited, unprocessed sample to be analyzed. The other is a known background signal, generally in a very narrow frequency band that can be used to time stamp the sample. The program will return if certain background frequencies of the sample also exist within the background, and if so, when.
#### Usage
`python cli.py c [sample file] [background data] [freq] [range]`
- c: Specifies compare mode. Can also be written as `compare`.
- sample file: Takes a relative path for the file from which data should be analyzed. Can be any file that contains audio data.
- background data: Takes a relative path for the file which contains historical background data with known recording time. Must be a .wav file.
- frequency: The core frequency in Hz that should be extracted from the sample.
- range: How many Hz in either direction from the core frequency should be accepted through the filter. This is not an exact measure due to how the filtering method works.
<!-- end list -->
The frequency range specified should be roughly equivalent to the expected frequency range of the background. For the US power grid, the frequency range of that signal is expected to be 60Hz +/- 1%[^1]. This means a reasonable frequency range for comparing against the background mains hum would be 60Hz +/- 0.6 Hz.
#### Ouput
Prints whether a match was found between the sample and the background, and at what sample point in the background file does the match start.
## Citations
[^1]:Muelaner, J. (2021, February 5). Grid frequency stability and renewable power. Engineering.com. https://www.engineering.com/grid-frequency-stability-and-renewable-power/
