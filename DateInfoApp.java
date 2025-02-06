import java.awt.*;
import java.time.LocalDate;
import java.time.temporal.ChronoField;
import javax.swing.*;

public class DateInfoApp {
    public static void main(String[] args) {
        String message = getDateInfo();
        createAndShowGUI(message);
    }

    private static String getDateInfo() {
        LocalDate today = LocalDate.now();
        int year = today.getYear();
        int dayOfYear = today.getDayOfYear();
        int weekOfYear = today.get(ChronoField.ALIGNED_WEEK_OF_YEAR);
        int daysRemaining = today.lengthOfYear() - dayOfYear;

        return String.format("当前日期: %s\n" +
                             "当前年份: %d\n" +
                             "今天是今年的第 %d 天\n" +
                             "今天是第 %d 周\n" +
                             "今年还剩下 %d 天",
                             today, year, dayOfYear, weekOfYear, daysRemaining);
    }

    private static void createAndShowGUI(String message) {
        JFrame frame = new JFrame("日期信息");
        JTextArea textArea = new JTextArea(message);
        textArea.setEditable(false);
        frame.add(new JScrollPane(textArea), BorderLayout.CENTER);
        frame.setSize(300, 200);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLocationRelativeTo(null); // Center the window
        frame.setVisible(true);
    }
}
