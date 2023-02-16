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
let g:deoplete#enable_at_startup = 1
let g:Hexokinase_highlighters = ['virtual']
Plug 'davidhalter/jedi-vim'
if has('nvim')
Plug 'Shougo/deoplete.nvim', { 'do': ':UpdateRemotePlugins' }
else
Plug 'Shougo/deoplete.nvim'
Plug 'roxma/nvim-yarp'
Plug 'roxma/vim-hug-neovim-rpc'
endif
call plug#end()
