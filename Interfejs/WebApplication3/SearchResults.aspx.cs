using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.Text.RegularExpressions;

namespace WebApplication3
{
    public partial class SearchResults : System.Web.UI.Page
    {
 

        protected void Page_Load(object sender, EventArgs e)
        {
            if (!IsPostBack)
                BindList();
        }

        private void BindList()
        {
            List<MyImage> list = new List<MyImage>
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

}