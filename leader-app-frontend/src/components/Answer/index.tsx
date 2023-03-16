import { useBaseQuery } from "@/hooks/useCustomQuery";
import * as React from "react";
import HorizontalBar from "../HorizontalBar";
import styles from "./Answer.module.scss";

interface ISingleAnswer {
  label: string;
  percentage_of_vote_so_far: number;
  percentage_of_vote_so_far_with_t: string;
  percentage_round_participants: number;
  total: number;
}

const Answer = () => {
  const { data: items, refetch } = useBaseQuery<ISingleAnswer[]>("/live/tally");

  React.useEffect(() => {
    const interval = setInterval(() => {
      refetch();
    }, 500);

    return () => clearInterval(interval);
  }, [refetch]);

  const totalVotes = React.useMemo(() => {
    if (!items) return 0;
    return items.reduce((acc, item) => acc + item.total, 0);
  }, [items]);

  if (!items) return null;

  return (
    <div className={styles.root}>
      {items.map((item, index) => (
        <HorizontalBar
          key={item.label}
          votes={item.total}
          label={item.label}
          index={index}
          width={(item.total / totalVotes) * 100}
        />
      ))}
    </div>
  );
};

export default Answer;
