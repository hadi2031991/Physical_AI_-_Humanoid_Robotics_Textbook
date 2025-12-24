import type {ReactNode} from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';

import Heading from '@theme/Heading';

import styles from './index.module.css';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero', styles.heroBanner)}>
      <div className="container">
        <div className={styles.heroContent}>
          <div className={styles.heroImage}>
            <img src="img/hq720.jpg" alt="Physical AI and Humanoid Robotics" />
          </div>
          <div className={styles.heroText}>
            <Heading as="h1" className={styles.heroTitle}>
              {siteConfig.title}
            </Heading>
            <p className={styles.heroSubtitle}>{siteConfig.tagline}</p>
            <div className={styles.buttons}>
              <Link
                className="button button--primary button--lg"
                to="/docs/part1/ch1">
                Start Reading
              </Link>
              <Link
                className="button button--secondary button--lg"
                to="/docs/part1/ch2">
                Explore Content
              </Link>
            </div>
          </div>
        </div>
      </div>
    </header>
  );
}

export default function Home(): ReactNode {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`Welcome to ${siteConfig.title}`}
      description="Physical AI & Humanoid Robotics Textbook">
      <HomepageHeader />
      <main>
        <div className={styles.featuresSection}>
          <div className="container">
            <div className={styles.featuresGrid}>
              <Link className={styles.featureCardLink} to="/docs/part1/ch1">
                <div className={styles.featureCard}>
                  <div className={styles.featureCardImage}>
                    <img src="img/pai.jpg" alt="Foundations of Physical AI" />
                  </div>
                  <h3>Foundations of Physical AI</h3>
                  <p>Understanding the core principles that govern embodied intelligence systems.</p>
                </div>
              </Link>
              <Link className={styles.featureCardLink} to="/docs/part2/ch5">
                <div className={styles.featureCard}>
                  <div className={styles.featureCardImage}>
                    <img src="img/air.jpg" alt="Intelligence for Robots" />
                  </div>
                  <h3>Intelligence for Robots</h3>
                  <p>Advanced AI algorithms designed specifically for robotic applications.</p>
                </div>
              </Link>
              <Link className={styles.featureCardLink} to="/docs/part3/ch9">
                <div className={styles.featureCard}>
                  <div className={styles.featureCardImage}>
                    <img src="img/hmr.jpg" alt="Building Humanoid Robots" />
                  </div>
                  <h3>Building Humanoids</h3>
                  <p>Practical approaches to designing and programming humanoid robots.</p>
                </div>
              </Link>
            </div>
          </div>
        </div>
      </main>
    </Layout>
  );
}