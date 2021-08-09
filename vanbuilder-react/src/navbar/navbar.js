import React from 'react'
import Container from 'react-bootstrap/Container'
import logo from '../icons/logos/Logo-white-text.png'
import Navbar from 'react-bootstrap/Navbar'
import NavDropdown from 'react-bootstrap/NavDropdown'
import Nav from 'react-bootstrap/Nav'

export function navbar() {
  
  return <Navbar collapseOnSelect expand="lg" variant='dark'>
    <Container>
      <Navbar.Brand href="#home">
        <img src={logo} className="App-logo" alt="logo" />
      </Navbar.Brand>
      <Navbar.Toggle aria-controls="responsive-navbar-nav" />
      <Navbar.Collapse id="responsive-navbar-nav">
        <Nav className="ml-auto" >
          <NavDropdown title="Build" id="collasible-nav-dropdown">
            <NavDropdown.Item href="#builds">Your Builds</NavDropdown.Item>
            <NavDropdown.Item href="#vans">Vans</NavDropdown.Item>
            <NavDropdown.Item href="#components">Components</NavDropdown.Item>
          </NavDropdown>
          <NavDropdown title="About" id="collasible-nav-dropdown">
            <NavDropdown.Item href="#about">About</NavDropdown.Item>
            <NavDropdown.Item href="#contact">Contact</NavDropdown.Item>
            <NavDropdown.Item href="#donate">Donate</NavDropdown.Item>
          </NavDropdown>
          <Nav.Link href="#login">Login / Signup</Nav.Link>
        </Nav>
      </Navbar.Collapse>
    </Container>
  </Navbar>
}