using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using System.Globalization;

namespace BasketStats
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }
        public DateTime startTime;


        private void BackGround_Click(object sender, RoutedEventArgs e)
        {
            double X = Mouse.GetPosition(this).X;
            double Y = Mouse.GetPosition(this).Y;
            string playerId = PlayerTxt.Text;
            PlayerTxt.Clear();
            var isHome = Home.IsChecked;
            DateTime currentTime = DateTime.Now;
            TimeSpan scoreTime = currentTime.Subtract(startTime);
            scoreTime.ToString("h'h 'm'm 's's'");
        }

        public void start_Click(object sender, RoutedEventArgs e)
        {
            startTime = DateTime.Now;
        }

        
        private void finish_Click(object sender, RoutedEventArgs e)
        {
            DateTime finishTime = DateTime.Now;
        }
    }
}
