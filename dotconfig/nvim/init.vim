call plug#begin('~/.vim/plugged')

set mouse=a

filetype on
syntax on

set number relativenumber
set ignorecase
set smartcase
set wildmenu
set termguicolors

Plug 'rrethy/vim-hexokinase', {'do': 'make hexokinase'}
Plug 'morhetz/gruvbox'
Plug 'roxma/nvim-yarp'
Plug 'roxma/vim-hug-neovim-rpc'

let g:Hexokinase_highlighters = ['virtual']

autocmd vimenter * ++nested colorscheme gruvbox

call plug#end()
