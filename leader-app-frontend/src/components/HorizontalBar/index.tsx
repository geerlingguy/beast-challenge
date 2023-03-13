import * as React from "react";
import styles from "./HorizontalBar.module.scss";
import { motion } from "framer-motion";

interface Props {
  width: number;
  votes: number;
  index: number;
  label: string;
}

const HorizontalBar = ({ width, votes, index, label }: Props) => {
  const rootBackground = React.useMemo(() => {
    switch (index) {
      case 0:
        return "linear-gradient(280deg, rgb(255, 97, 154) 0%, rgb(255, 107, 178) 100%)";
      case 1:
        return "linear-gradient(280deg, #FFBE41 27.43%, #F8EF22 97.7%)";
      case 2:
        return "linear-gradient(280deg, #FF7222 0%, #FF8422 98.3%)";
      default:
        break;
    }
  }, [index]);

  const background = React.useMemo(() => {
    switch (index) {
      case 0:
        return "linear-gradient(90deg, #FF619A 0%, #FF6BB2 100%)";
      case 1:
        return "linear-gradient(90deg, #FFBE41 27.43%, #F8EF22 97.7%)";
      case 2:
        return "linear-gradient(90deg, #FF7222 0%, #FF8422 98.3%)";
      default:
        break;
    }
  }, [index]);

  const barColor = React.useMemo(() => {
    switch (index) {
      case 0:
        return "linear-gradient(180deg, #C22E64 0%, #D94479 100%)";
      case 1:
        return "linear-gradient(235.41deg, #E6951C -11.74%, #ECC436 40.81%)";
      case 2:
        return "linear-gradient(180deg, #D95105 0%, #E06D11 98.3%)";
      default:
        break;
    }
  }, [index]);

  return (
    <div className={styles.container}>
      <div style={{ background: rootBackground }} className={styles.root}>
        <p className={styles.answer}>{label}</p>
        <p className={styles.votes}>{votes} votes</p>
      </div>
      <motion.div
        initial={{ width: 0 }}
        animate={{ width: `${width}%` }}
        // transition={{ ease: [0.17, 0.67, 0.83, 0.67] }}
        // transition={{ type: "spring", bounce: 0.25 }}
        transition={{ type: "inertia", velocity: 100 }}
        // transition={{
        //   duration: 0.05,
        //   type: "spring",
        //   damping: 3,
        //   stiffness: 150,
        //   restDelta: 0.001,
        // }}
        style={{ background }}
      ></motion.div>
      <div
        className={styles.bar}
        style={{
          background: barColor,
        }}
      />
    </div>
  );
};

export default HorizontalBar;
