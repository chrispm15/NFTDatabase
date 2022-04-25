# NFTDatabase
Grabs data from OpenSea and appends it to a Google Sheet.

#how-to

  - Obtain a Google .json authorization file
  - Enable both Google Sheets and Google Drive API
  - Change the variable 'collections' to define which collections you wish to track
  - Create a Google Sheets with 4 worksheets ('floor prices', 'volume', 'sales', 'holders', 'avg. holder')
  - On each sheet, name columns in the following way: ('date', {collection}, {collection2}, {collection3), etc)
      - The collections should match those defined in your variable 'collections' and should be in the same order
  - Run the script to obtain data and post it to your Google Sheets
