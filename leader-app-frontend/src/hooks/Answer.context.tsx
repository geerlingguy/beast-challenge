import * as React from "react";

interface Props {
  labelWidth?: number;
  resetWidth(): void;
  handleWidthChange(newWidth: number): void;
}
const AnswerContext = React.createContext<Props>({
  labelWidth: undefined,
  resetWidth: () => {},
  handleWidthChange: () => {},
});

export const AnswerProvider = ({ children }: { children: React.ReactNode }) => {
  const [labelWidth, setLabelWidth] = React.useState<number | undefined>(
    undefined
  );
  const handleWidthChange = React.useCallback(
    (newWidth: number) => {
      if (newWidth > (labelWidth || 0)) {
        setLabelWidth(newWidth);
      }
    },
    [labelWidth]
  );

  const resetWidth = React.useCallback(() => {
    setLabelWidth(undefined);
  }, []);

  return (
    <AnswerContext.Provider
      value={{ labelWidth, handleWidthChange, resetWidth }}
    >
      {children}
    </AnswerContext.Provider>
  );
};

export const useAnswer = () => React.useContext(AnswerContext);
