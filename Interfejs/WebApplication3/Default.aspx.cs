using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace WebApplication3
{
    public partial class _Default : Page
    {
        List<MyImage> list;
        protected void Page_Load(object sender, EventArgs e)
        {
            if (!IsPostBack)
                BindList();
        }

        private void BindList()
        {
            list= new List<MyImage>
            {
                new MyImage (1,"Content/Images/abstract.jpg","tit"),
                new MyImage(2, "Content/Images/unnamed.jpg", "tit2"),
                new MyImage (3,"Content/Images/abstract.jpg","tit3"),
                new MyImage(4, "Content/Images/unnamed.jpg", "tit4"),
                new MyImage (5,"Content/Images/abstract.jpg","tit"),
                new MyImage (6,"Content/Images/abstract.jpg","tit"),
                new MyImage(7, "Content/Images/unnamed.jpg", "tit2"),
                new MyImage (8,"Content/Images/abstract.jpg","tit3"),
                new MyImage(9, "Content/Images/unnamed.jpg", "tit4")
            };
            Repeater1.DataSource = list;
            Repeater1.DataBind();
            
        }


    };

    public class MyImage
    {
        public MyImage(int Id,string Src,string Tit)
        {
        id = Id;
        src = Src;
        title = Tit;
        }
        public int id { get; set; }
        public string src { get; set; }
        public string title { get; set; }
    };

}