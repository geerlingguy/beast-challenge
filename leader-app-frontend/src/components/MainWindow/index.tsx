import * as React from "react";
import Answer from "../Answer";
import styles from "./MainWindow.module.scss";
import cs from "classnames";
import { useRouter } from "next/router";
import { AnswerProvider } from "@/hooks/Answer.context";
const MainWindow = () => {
  const router = useRouter();
  const { is_green } = router.query;
  return (
    <AnswerProvider>
      <div className={styles.root}>
        <div
          className={cs(styles.background, {
            [styles.background__green]: is_green === "true",
          })}
        />
        <Answer />
      </div>
    </AnswerProvider>
  );
};

export default MainWindow;
