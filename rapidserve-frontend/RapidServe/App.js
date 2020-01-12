import React, { Component } from 'react';
import { StyleSheet, Text, View, Image, TouchableOpacity, AsyncStorage, ActivityIndicator, Alert, StatusBar } from 'react-native';
import Welcome from "./screens/Welcome";
import logo from "./images/logo.png"
import logo2 from "./images/logo2.png"
import * as Facebook from "expo-facebook";
import { createAppContainer, createSwitchNavigator } from "react-navigation";
import { createStackNavigator } from "react-navigation-stack";

const id = "407364903529255";

class AuthLoadingScreen extends Component {
  componentDidMount() {
    this._bootstrapAsync();
  }

  _bootstrapAsync = async () => {
    const userId = await AsyncStorage.getItem("myId");
    this.props.navigation.navigate(userId ? "App" : "Auth");
  };

  render() {
    return (
      <View>
        <ActivityIndicator />
        <StatusBar barStyle = "default"/>
      </View>
    );
  }
}

class SignInScreen extends React.Component {
  static navigationOptions = {
    title: "",
    headerTintColor: "white",
    headerStyle: {
      backgroundColor: "#292E30",
    },
    headerBackTitleStyle: {
        color: "white",
        fontWeight: "bold"
    },
    headerBackImageStyle: {
        tintColor: "white",
    }
  };

  request = async (url,method,body) => {
    return new Promise((resolve,reject) => {
      if (method === 'GET') {
        console.log('GOT1');
        fetch(url)
        .then(response => {
          console.log('START1');
          if(response.headers.get("content-length") == 0) {
            return 0;
          }
          var responseJson = response.json();
          console.log('END');
          return responseJson;
        })
        .then(data => {
          console.log('GOT2');
          resolve(data)
          console.log('GOOOTEEM');
        })
        .catch(err => {
          console.log('GOT3');
          reject(err)
        });
      } else {
        fetch(url, {
          method: method,
          headers: {
            Accept: 'application/json',
            'content-type': 'application/json',
          },
          body: body
        }).then(response => response.json())
        .then(data => resolve(data))
        .catch(err => reject(err));
      }
    });
  }

  logIn = async () => {
    await Facebook.initializeAsync(id);
    const {
      type,
      token
    } = await Facebook.logInWithReadPermissionsAsync({
      permissions: ["public_profile", "email"],
    });
    if(type === 'success') {
      const response = await fetch(
        `https://graph.facebook.com/me?access_token=${token}&fields=id,name,email`
      );

      const json = await response.json();
      console.log('HEEEEEEDASDWD');
      this.request('http://34.83.193.124/users/api/v1.0/exists/' + json.id, 'GET')
      .then( (user)  => {
        if(user) {
          AsyncStorage.setItem("myId", user.user_id).then( () => {
            Alert.alert('Logged in!', `Hi ${user.full_name}!`);
            this.presentApp();
          });
        } else {
          const jsonBody =  {
            user_id: json.id,
            full_name: json.name,
            phone_number: "0",
            credit: 100.0,
            email: json.email,
            restaurant_id: 12345,
            table_id: 0,
            role: 0,
          };
          this.request('http://34.83.193.124/users/api/v1.0/register', 'POST', JSON.stringify(jsonBody)
          ).then( (user) => {
            console.log('EYYYY');
            AsyncStorage.setItem("myId", user.user_id).then( () => {
              console.log('HEYYYY');
              Alert.alert('Logged in!', `Hi ${user.full_name}!`);
              this.presentApp();
            });
          })
        }
      })
    } else {
      // type === "cancel"
      Alert.alert('Error encountered', 'Sorry!');
    }
  }

  presentApp() {
    this.props.navigation.navigate("App");
  }

  render() {
    return (
      <View style={styles.container}>
        <Image style = {styles.logo2} source = {logo2} />
        <Image style = {styles.logo} source={logo} />
        <TouchableOpacity onPress = {() => this.logIn()}>
          <View style = {{width: "70%", borderRadius: 10, padding: 24, backgroundColor: "#13C0EB", justifyContent: "center", alignItems: "center" }}>
              <Text style = {{color: "#FFFFFF", fontWeight: "bold", fontSize: 20}}>Facebook Log-in</Text>
          </View>
        </TouchableOpacity>
        {/* <Welcome/> */}
      </View>
    );
  }
}

const AuthStack = createStackNavigator({
  SignIn: SignInScreen,
});

const AppContainer = createAppContainer(
  createSwitchNavigator(
    {
      AuthLoading: AuthLoadingScreen,
      Auth: AuthStack,
      App: Welcome,
    },
    {
      initialRouteName: "AuthLoading",
    }
  )
);


export default class App extends Component {
  navigator;

  constructor(props) {
    super(props);
  }

  render() {
    return (<AppContainer ref={(nav) => { this.navigator = nav; }}/>);
  }

}

const styles = StyleSheet.create({
  container: {
    paddingTop: 50,
    flex: 1,
    backgroundColor: '#292E30',
    alignItems: 'center',
  },
  logo: {
    width: 375,
    height: 100,
    resizeMode: "stretch",
    marginBottom: 160,
  },
  logo2: {
    width: 100,
    height: 100,
    resizeMode: "stretch",
  }
});
