import React, { useState, useEffect } from 'react';
import Link from '@docusaurus/Link';
import { useLocation } from '@docusaurus/router';
import { useThemeConfig } from '@docusaurus/theme-common';
import useBaseUrl from '@docusaurus/useBaseUrl';
import SearchBar from '@theme/SearchBar';
import styles from './styles.module.css';

const CustomNavbar = () => {
  const location = useLocation();
  const [isScrolled, setIsScrolled] = useState(false);
  const themeConfig = useThemeConfig();
  const { title, logo = { src: '' }, items = [] } = themeConfig.navbar;

  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 10);
    };

    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const logoLink = logo.href || '/';
  const logoSrc = useBaseUrl(logo.src);

  return (
    <nav className={`navbar navbar--fixed-top ${styles.navbar} ${isScrolled ? styles.navbarScrolled : ''}`}>
      <div className="navbar__inner container">
        <div className="navbar__items">
          <Link className={`navbar__brand ${styles.navbarBrand}`} to={logoLink}>
            {logo && (
              <img
                className={`navbar__logo ${styles.navbarLogo}`}
                src={logoSrc}
                alt={logo.alt}
              />
            )}
            <span className={`navbar__title ${styles.navbarTitle}`}>
              {title}
            </span>
          </Link>
          {items
            .filter(item => item.position === 'left')
            .map((item, index) => (
              <NavbarItem key={index} {...item} location={location} />
            ))}
        </div>
        <div className="navbar__items navbar__items--right">
          <SearchBar />
          {items
            .filter(item => item.position === 'right')
            .map((item, index) => (
              <NavbarItem key={index} {...item} location={location} />
            ))}
        </div>
      </div>
    </nav>
  );
};

const NavbarItem = ({ type, to, href, label, position, location, ...props }) => {
  const isExternalLink = href && !href.startsWith('/');
  const isCurrentPage = location.pathname === to;

  if (type === 'search') {
    return <SearchBar />;
  }

  if (isExternalLink) {
    return (
      <a
        className="navbar__item navbar__link"
        href={href}
        target="_blank"
        rel="noopener noreferrer"
      >
        {label}
      </a>
    );
  }

  return (
    <Link
      className={`navbar__item navbar__link ${isCurrentPage ? 'navbar__link--active' : ''}`}
      to={to}
    >
      {label}
    </Link>
  );
};

export default CustomNavbar;