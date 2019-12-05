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
using MySql.Data;
using MySql.Data.MySqlClient;
using System.Configuration;

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
        public static string ConnStr = ConfigurationManager.ConnectionStrings["MySql"].ToString();
        public MySqlConnection con = new MySqlConnection(ConnStr);

        private void BackGround_Click(object sender, RoutedEventArgs e)
        {
            Dictionary<string, object> statDict = new Dictionary<string, object>();

            double X = Mouse.GetPosition(this).X;
            double Y = Mouse.GetPosition(this).Y;
            string playerId = PlayerTxt.Text;
            PlayerTxt.Clear();
            string score = ScoreTxt.Text;
            ScoreTxt.Clear();
            int isHome;
            if (Home.IsChecked == true)
            {
                isHome = 1;
            }
            else
            {
                isHome = 0;
            }
            DateTime currentTime = DateTime.Now;
            TimeSpan scoreTime = currentTime.Subtract(startTime);
            string strScoreTime = scoreTime.ToString("h'h 'm'm 's's'");

            statDict.Add("playerId", playerId);
            statDict.Add("score", score);
            statDict.Add("X", X);
            statDict.Add("Y", Y);
            statDict.Add("isHome", isHome);
            statDict.Add("scoreTime", strScoreTime);

            try
            {
                con.Open();
            }
            catch(MySqlException ex)
            {
                string message = ex.Message;
            }

            string query = "INSERT INTO AppStatistic(PlayerID,Score,PositionX,PositionY,IsHome,ScoreTime) VALUES(" + "'" +statDict["playerId"] + "'" + "," + "'" + statDict["score"]+ "'" + "," + "'" + statDict["X"]+ "'" + "," + "'" + statDict["Y"]+ "'" + "," + "'" + statDict["isHome"] + "'" + "," + "'" + strScoreTime + "'" +")" ;
            MySqlCommand cmd = new MySqlCommand(query, con);
            cmd.ExecuteNonQuery();
            con.Close();


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
