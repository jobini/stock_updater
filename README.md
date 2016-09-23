<h1><b>Stock price collector</b></h1>

<h2><b>Synopsis</b></h2>

These are Python scripts to periodically append stock-related information of a given list of companies, collected using the `googlefinance` module, to a CSV file.

<h2><b>Requirements</b></h2>

1. Python version 2.6+
2. [googlefinance]()
3. [pandas]()

<h2><b>Usage</b></h2>

The `google_finance.py` script accepts a periodicity (buffer time between fetching) in seconds, and appends `AppendTime`,`Index`,`LastTradePrice`,`LastTradeDateTimeLong`, `StockSymbol` and `ID` to a CSV file. By default, the CSV file is named `sample_portfolio.csv`. To change this, set the `file_name` variable in the script file, to a file name that you'd like. To test the script, simply run `python google_finance.py` in the Terminal, from the directory of the extracted files. To see a sample output, view the `output.csv` file in this repository.

The `google_finance_mod.py` script provides a template to periodically append one particular stock attribute sideways in a CSV, so as to facilitate better data analysis. It requires a `companies.csv` file, which is a CSV file containing a list of company names and corresponding stock symbols, which are to be analyzed. To see its template, view the `companies.csv` file in this repository. The output is named based on the time at which the script is run, to facilitate better data organization. To test the script, simply run `python google_finance_mod.py` in the Terminal, from the directory of the extracted files. To see a sample output, view the `output_mod.csv` file in this repository.

<h2><b>To add</b></h2>

1. Better optimization using [pandas]()
2. Pause/resume in same file

<h2><b>License</b></h2>

Please view LICENSE.md for details on the usage of code in this repository.
