mkdir -p ~/.streamlit/

echo "\
[theme]\n\
primaryColor = ‘#F63366’\n\
backgroundColor = ‘#fef8ef’\n\
secondaryBackgroundColor = ‘#ebd2b9’\n\
textColor= ‘#262730’\n\
font = ‘serif’\n\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\ 
" > ~/.streamlit/config.toml