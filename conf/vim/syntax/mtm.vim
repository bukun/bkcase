" meeting munites plugin
" Author: Aaron Wu
" initial: 2007/07/26 四 
" OS: windows
" install:
" put two files to the related directory.
" syntax/mtm.vim
" ftdetect/mtm.vim
"
" usage:
" 1. use the mtm suffix of the file like: e:/meeting.mtm
" 2. the meeting.mtm is like that:
" 
"       Title: title
"       Date: 2007/07/26 四 
"       Time: 11:54
"       Location: 大会议室
"       Minutes:
"         1. ...
"         2. ...
"
" 3. hot keys
" ,a to add a meeting item
"
" 4. folding and highlight
" can fold by a meeting.
"
syn match title "^Title:.*"                
syn match date "^Date:"
syn match time "^Time:"
syn match location "^Location:"
syn match minutes "^Minutes:"
syn match dateno "\d\d\d\d/\d\d/\d\d .*"
syn match timeno "\d\{1,2}:\d\d"
hi title guifg=lightred gui=bold
hi date guifg=lightyellow 
hi time guifg=lightyellow 
hi location guifg=lightyellow 
hi minutes guifg=lightblue 
hi dateno guifg=lightgreen 
hi timeno guifg=lightgreen

setl fdm=expr
setl fdc=3
setl foldexpr=Myindent(v:lnum)
func! Myindent(lnum)
  if (strlen(matchstr(getline(v:lnum), '^Minutes:')) != 0)
    return '>2'
  elseif (strlen(matchstr(getline(v:lnum), '^Title:')) != 0)
    return '>1'
  else
    return '='
  endif
endf

abb ,a Title:<CR>Date: <ESC>:r! date /t<CR>kJoTime: <ESC>:r! time /t<CR>kJoLocation: <CR>Minutes:<ESC>kkkkA
ftdetect/mtm.vim
au BufNewFile,BufRead *.mtm     setf mtm
