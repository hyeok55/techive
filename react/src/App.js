import logo from './logo.svg';
import './home.css';

import React from 'react';
import RestAPI from './RestAPI';  // RestAPI 컴포넌트를 불러옵니다.

function Header() {
  return (
      <header>
          <div className="logo">
              <img src="/img/company_logo.png" alt="회사 로고" />
          </div>
          <div className="search">
              <div className="search-input">
                  <span id="search-icon">&#128269;</span>
                  <input type="text" id="search-box" placeholder="Search" />
              </div>
          </div>
      </header>
  );
}

function MainContent() {
  return (
      <main>
          <section className="dashboard">
              <div className="dashboard-title">
                  <h1>IT 직군 트렌드 분석</h1>
              </div>
              <div className="dashboard-buttons">
                  <button id="all-button" className="active">전체</button>
                  <button id="company-button">기업별</button>
                  <div id="chart-container"></div>
              </div>
          </section>
      </main>
  );
}

function App() {
  return (
      <div>
          <Header />
          <MainContent />
          <RestAPI />
      </div>
  );
}

export default App;
