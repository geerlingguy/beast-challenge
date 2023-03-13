import * as React from "react";
import Answer from "../Answer";
import Question from "../Question";
import styles from "./MainWindow.module.scss";

const MainWindow = () => {
  return (
    <div className={styles.root}>
      <div className={styles.background} />
      <Question question="What's your favorite animal?" timeLimit={60000} />
      <Answer />
    </div>
  );
};

export default MainWindow;
