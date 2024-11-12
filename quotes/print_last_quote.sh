#!/bin/bash

# Clear or create the log files
> quotes_base64.log
> quotes.log

osascript <<EOF
tell application "Notes"
    set quotesFolder to folder "Quotes"
    if exists quotesFolder then
        set allNotes to notes of quotesFolder
        if length of allNotes is greater than 0 then
            repeat with currentNote in allNotes
                set noteContent to (get the plaintext of currentNote as text)
                do shell script "echo " & quoted form of noteContent & " | base64 >> quotes_base64.log"
            end repeat
        end if
    end if
end tell
EOF

# Decode the base64 content and save to quotes.log
while IFS= read -r line; do
    echo "-------------------" >> quotes.log
    echo "$line" | base64 -d >> quotes.log
    echo "" >> quotes.log
done < quotes_base64.log

# Clean up the temporary base64 file
rm quotes_base64.log