using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.RegularExpressions;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace WebApplication3
{
    public partial class Details : Page
    {
        enum Category
        {
            Nieznane,
            Realizm,
            Surrealizm,
            Romantyzm
        }
        enum Technique
        {
            Nieznane,
            Olej,
            Akwarela,
            Akryl
        }
        Dictionary<String, Category> categories = new Dictionary<string, Category>
        {
            {"NIEZNANE",Category.Nieznane },
            {"REALIZM", Category.Realizm },
            {"SURREALIZM", Category.Surrealizm },
            {"ROMANTYZM",Category.Romantyzm }
        };
        Dictionary<String, Technique> techniques = new Dictionary<string, Technique>
        {
            {"NIEZNANE",Technique.Nieznane },
            {"OLEJ", Technique.Olej },
            {"AKWARELA", Technique.Akwarela },
            {"Akryl",Technique.Akryl }
        };
        private Category getCategoryByName(String name)
        {
            Category cat;
            return categories.TryGetValue(name.ToUpper(), out cat) ? cat : Category.Nieznane;
        }
        private Technique getTechniqueByName(String name)
        {
            Technique tech;
            return techniques.TryGetValue(name.ToUpper(), out tech) ? tech : Technique.Nieznane;
        }
        private void LoadData(String dest)
        {
            String name = "Nieznane";
            String birth = "Nieznane";
            String birthPlace = "Nieznane";
            String death = "Nieznane";
            String deathPlace = "Nieznane";
            String museum = "Nieznane";
            String education = "Nieznane";
            List<Category> cats = new List<Category>();
            List<Technique> techs = new List<Technique>();
            List<String> res = new List<String>();
            Regex rex = new Regex("(?<=<)(.*?)(?=>)");
            String findData(String dataTag, StreamReader sr)
            {
                sr.BaseStream.Position = 0;
                sr.DiscardBufferedData();
                String line = "Nieznane";
                while ((line = sr.ReadLine()) != null)
                {
                    if (line == dataTag)
                    {
                        line = sr.ReadLine();
                        line = rex.Match(line).ToString();
                        break;
                    }
                }
                return line;
            }
            List<String> findAllData(String dataTag, StreamReader sr)
            {
                sr.BaseStream.Position = 0;
                sr.DiscardBufferedData();
                String line = "Nieznane";
                List<String> results = new List<String>();
                while ((line = sr.ReadLine()) != null)
                {
                    if (line == dataTag)
                    {
                        while (((line = sr.ReadLine()) != null) && rex.IsMatch(line))
                        {
                            line = rex.Match(line).ToString();
                            results.Add(line);
                        }
                        break;
                    }
                }
                return results;
            }
            try
            {
                dest = AppDomain.CurrentDomain.BaseDirectory + "\\" + dest;
                using (StreamReader sr = new StreamReader(dest))
                {
                    name = findData("[Name]:", sr);
                    birth = findData("[Birth Date]:", sr);
                    birthPlace = findData("[Birth Place]:", sr);
                    death = findData("[Death Date]:", sr);
                    deathPlace = findData("[Death Place]:", sr);
                    res = findAllData("[Categories]:", sr);
                    foreach(String result in res)
                        cats.Add(getCategoryByName(result));
                    res = findAllData("[Techniques]:", sr);
                    foreach (String result in res)
                        techs.Add(getTechniqueByName(result));
                    museum = findData("[Museum]:", sr);
                    education = findData("[Education]:", sr);
                }
            }
            catch (Exception ex)
            {
                //Well, fuck
            }
            Name.Text = "Imię: " + name +"<br/>";
            Birth.Text = "Urodzony: " + birth + " w " + birthPlace + " <br/>";
            Death.Text = "Zmarł: " + death + " w " + deathPlace +" <br/>";
            Style.Text = "Styl: ";
            foreach (Category cat in cats)
                Style.Text += Enum.GetName(typeof(Category), cat) + ", ";
            Style.Text += "<br/>";
            Tech.Text = "Technika: ";
            foreach (Technique tech in techs)
                Tech.Text += Enum.GetName(typeof(Technique), tech) + ", ";
            Tech.Text += "<br/>";
        }
        protected void Page_Load(object sender, EventArgs e)
        {
            LoadData("..\\..\\files_stuff\\result\\result.txt");
        }

        protected void Menu1_MenuItemClick(object sender, MenuEventArgs e)
        {
            int i = Int32.Parse(e.Item.Value);
            MultiView1.ActiveViewIndex = i;
            if(Menu1.SelectedItem!=null)
                Menu1.SelectedItem.Selected = false;
            Menu1.Items[i].Selected = true;
        }
    }
}