import * as React from "react";
import { motion } from "framer-motion";
import Countdown, { CountdownRenderProps } from "react-countdown";
import styles from "./Question.module.scss";
import FlashIcon from "../../assets/flash.png";
import Image from "next/image";

const Question = ({
  question,
  timeLimit,
}: {
  question: string;
  timeLimit: number;
}) => {
  // Renderer callback with condition
  const renderer = (props: CountdownRenderProps) => {
    return (
      <span>
        {props.formatted.minutes}:{props.formatted.seconds}
      </span>
    );
  };

  return (
    <motion.div
      initial={{ x: "-100%" }}
      animate={{ x: 0 }}
      transition={{ duration: 0.5 }}
    >
      <div className={styles.root}>
        <div className={styles.flash}>
          <Image
            src={FlashIcon.src}
            height={FlashIcon.height}
            width={FlashIcon.width}
            alt="flash"
          />
        </div>
        <div className={styles.question}>{question}</div>
        <div className={styles.timer}>
          <Countdown renderer={renderer} date={Date.now() + timeLimit} />
        </div>
      </div>
    </motion.div>
  );
};

export default Question;
