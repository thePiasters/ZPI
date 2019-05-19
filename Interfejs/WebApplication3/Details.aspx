<%@ Page Title="DetailsPage" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="Details.aspx.cs" Inherits="WebApplication3.Details" %>

<asp:Content runat="server" ContentPlaceHolderID="MainContent">
            <asp:Menu ID="Menu1" runat="server" Orientation="Horizontal" OnMenuItemClick="Menu1_MenuItemClick">
                <staticmenuitemstyle HorizontalPadding="10px" BackColor="#8298ff" BorderWidth="2px" BorderColor="Black" BorderStyle="Ridge"/>
                <staticselectedstyle HorizontalPadding="10px" BackColor="#c4c5ff" BorderWidth="2px" BorderColor="Black" BorderStyle="Ridge"/>
                <Items>
                    <asp:MenuItem Text="Dane osobowe" Value="0" Selected="true"></asp:MenuItem>
                    <asp:MenuItem Text="Kariera i edukacja" Value="1" ></asp:MenuItem>
                    <asp:MenuItem Text="Znane prace" Value="2"></asp:MenuItem>
                </Items>
            </asp:Menu>
        <div style="background-color:#959abb;height:100%">
            <asp:MultiView ID="MultiView1" runat="server" ActiveViewIndex="0">
                <asp:View ID="Tab1" runat="server">
                    <asp:Label ID="Name" runat="server" ></asp:Label>
                    <asp:Label ID="Birth" runat="server"></asp:Label>
                    <asp:Label ID="BirthDate" runat="server"></asp:Label>
                    <asp:Label ID="BirthPlace" runat="server"></asp:Label>
                    <asp:Label ID="Death" runat="server"></asp:Label>
                    <asp:Label ID="DeathPlace" runat="server"></asp:Label>
                    <asp:Label ID="Style" runat="server"></asp:Label>
                    <asp:Label ID="Tech" runat="server"></asp:Label>
                </asp:View>
                <asp:View ID="Tab2" runat="server">
                    <p>Kariera i edukacja!</p>
                </asp:View>
                <asp:View ID="Tab3" runat="server">
                    <p>Znane prace!</p>
                </asp:View>
            </asp:MultiView>
        </div>
</asp:Content>
