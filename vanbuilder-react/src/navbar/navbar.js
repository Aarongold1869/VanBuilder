import React from 'react'
import logo from '../icons/logos/Logo-white-text.png'

export function navbar(props) {

  return <nav id='navbar' className='navbar'>
      <a className='logo-link' alt='vanbuilder.com logo' href='#home'>
        <img id='nav-logo' className='nav-logo' src={logo} />
      </a>
      <ul id='nav-list' className='nav-list'>
        <li className='nav-list-item'><a classname='nav-link' href='#builds'>Builds</a></li>
        <li className='nav-list-item'><a classname='nav-link' href='#components'>Components</a></li>
        <li className='nav-list-item'><a classname='nav-link' href='#about'>About</a></li>
        <li className='nav-list-item'><a classname='nav-link' href='#contact'>Contact</a></li>
        <li className='nav-list-item'><a classname='nav-link' href='#profile'>Profile</a></li>
      </ul>
  </nav>
  
}