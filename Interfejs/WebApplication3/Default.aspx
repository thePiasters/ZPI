<%@ Page Title="Home Page" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="Default.aspx.cs" Inherits="WebApplication3._Default" %>

<asp:Content ID="DefaultContent" ContentPlaceHolderID="MainContent" runat="server">


<script type="text/javascript">
    function loadGraphics() {
        document.append('<img src="/path/to/image.jpg"
       width="16" height="16" alt="Test Image" title="Test Image" />');
    }
</script>
<style type="text/css">
    #gallery
    {
        
        padding: 10px;
        width: 100%;
        height:100%;
    }
    #gallery ul
    {
        list-style: none;
        display:flex;
        flex-direction:row;
        flex-wrap:wrap;
    }
    #gallery ul li
    {
        display:inline-block;
        height:220px;
    }
    #gallery ul li div
    {
        display: inline-block;
        height:180px;
        width:180px;

    }
    #gallery ul img
    {
        border: 5px solid #3e3e3e;
        border-width: 5px 5px 20px;
    }
    #gallery ul a:hover img
    {
        border: 5px solid #fff;
        border-width: 5px 5px 20px;
        color: #fff;
    }
    #gallery ul a:hover
    {
        color: #fff;
    }
</style>


    <div >
        <p style="text-align:center;">Popularne wśród naszych użytkowników</p>
        <div id="gallery">
            <asp:Repeater ID="Repeater1" runat="server">
                <HeaderTemplate>
                    <ul>
                        </HeaderTemplate>
                            <ItemTemplate>
                                <li>
                                    <div>

                                        <a runat="server" href='<%# String.Format("Details.aspx?dest={0}", Eval("title")) %>' title='<%# Eval("title") %>'>
                                            <div><img src='<%# Eval("src") %>' width="180" height="180" alt=""/></div>
                                            <div style="text-align:center">'<%# Eval("title") %>'</div>
                                           
                                        </a>
                                    </div>
                                </a></li>
                            </ItemTemplate>
                        <FooterTemplate>
                    </ul>
                </FooterTemplate>
            </asp:Repeater>
        </div>
    </div>
    

</asp:Content>
