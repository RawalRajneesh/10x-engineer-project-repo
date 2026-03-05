import Header from './Header';
import Sidebar from './Sidebar';

const Layout = ({ children }) => (
  <div className="app-layout">
    <Header />
    <Sidebar />
    <main>{children}</main>
  </div>
);

export default Layout;
