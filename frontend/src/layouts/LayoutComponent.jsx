import React from 'react';
import HeaderComponent from '../components/HeaderComponent';
import SidebarComponent from '../components/SidebarComponent';

const LayoutComponent = ({ children }) => {
  return (
    <div className="layout">
      <HeaderComponent />
      <SidebarComponent />
      <main>
        {children}
      </main>
    </div>
  );
};

export default LayoutComponent;