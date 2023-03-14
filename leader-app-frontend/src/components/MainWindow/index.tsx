import * as React from "react";
import Answer from "../Answer";
import styles from "./MainWindow.module.scss";
import cs from "classnames";
const MainWindow = () => {
  const isGreenScreen = false;
  return (
    <div className={styles.root}>
      <div
        className={cs(styles.background, {
          [styles.background__green]: isGreenScreen,
        })}
      />
      <Answer />
    </div>
  );
};

export default MainWindow;
