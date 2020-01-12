import * as React from 'react';
import { Text, View, StyleSheet, Button, TouchableOpacity } from 'react-native';
import Constants from 'expo-constants';
import * as Permissions from 'expo-permissions';
import { BarCodeScanner } from 'expo-barcode-scanner';

const styles = StyleSheet.create({
    TouchableOpacityScan: {
        width: "100%",
        height: "15%",
    },
    TextScan: {
        color: "#ffffff",
        fontSize: 30,
        textAlign: "center",
    },
    ViewScan: {
        width: "100%",
        height: "100%",
        backgroundColor: "#13C0EB",
        alignContent: "center",
        justifyContent: "center"
    },
    Scanner: {
        height: "85%",
        width: "100%",
    },
    TouchableOpacityConfirm: {
        width: "50%",
        height: "100%",
    },
    TextConfirm: {
        color: "#ffffff",
        fontSize: 30,
        textAlign: "center",
    },
    ViewConfirm: {
        width: "100%",
        height: "100%",
        backgroundColor: "#13C0EB",
        alignContent: "center",
        justifyContent: "center"
    },
    TouchableOpacityScanAgain: {
        width: "50%",
        height: "100%",
    },
    TextScanAgain: {
        color: "#ffffff",
        fontSize: 30,
        textAlign: "center",
    },
    ViewScanAgain: {
        width: "100%",
        height: "100%",
        backgroundColor: "#292E30",
        alignContent: "center",
        justifyContent: "center"
    },
    Bottom: {
        flexDirection: "row",
        height: "15%"
    },
    Row: {
        flexDirection: "row"
    },
    Box: {
        width: 300,
        height: 300,
        borderWidth: 10,
        borderColor: "#13C0EB",
        alignSelf: "center",
        marginTop: "35%",
        borderRadius: 30
    }
});

class Scan extends React.Component {
    state = {
        hasCameraPermission: null,
        scanned: false,
        tableId: null,
    };

    async componentDidMount() {
        this.getPermissionsAsync();
    }

    getPermissionsAsync = async () => {
        const { status } = await Permissions.askAsync(Permissions.CAMERA);
        this.setState({ hasCameraPermission: status === 'granted' });
    }

    handleBarCodeScanned = ({ data }) => {
        this.setState({ scanned: true });
        this.setState({tableId: data});
        alert(`Table ID: ${data} has been scanned!`);
    };

    putTableId = () => {
        const table = {
            table_id: this.state.tableId
        }
        fetch("http://34.83.193.124/users/api/v1.0/33333333333333333", {
            method: "PUT",
            headers: {'content-type': 'application/json'},
            body: JSON.stringify(table)
        }).then((response) => {
            alert('Put request gucci');
            // this.props.navigation.navigate("CustomerView", {
            //     tableId: response,
            // })
        }).catch(err => {
            console.log(err);
        })
    }

  render() {
    const { hasCameraPermission, scanned } = this.state;

    if (hasCameraPermission === null) {
      return <Text>Requesting permission of camera</Text>;
    }
    if (hasCameraPermission === false) {
      return <Text>Camera permission not granted</Text>;
    }
    return (
      <View
        style={{
          flex: 1,
          flexDirection: 'column',
          justifyContent: 'flex-end',
        }}>

        <View
            style={styles.TouchableOpacityScan}
            onPress={() => this.setState({ scanned: false })}
        >
            <View
                style={styles.ViewScan}
            >
                    <Text
                        style={styles.TextScan}
                    >
                        Scan A QR Code
                    </Text>
            </View>

        </View>

        <BarCodeScanner
          onBarCodeScanned={scanned ? undefined : this.handleBarCodeScanned}
          style={styles.Scanner}>

            <View style={styles.Box}>

            </View>
              
        </BarCodeScanner>   

        {!scanned &&(<View
            style={styles.TouchableOpacityScan}
            onPress={() => this.setState({ scanned: false })}
        >
            <View
                style={styles.ViewScan}
            >
                    <Text
                        style={styles.TextScan}
                    >
                        Scan A QR Code
                    </Text>
            </View>

        </View>)}

        {scanned &&(<View style={styles.Bottom}>

            {scanned && (<TouchableOpacity
                style={styles.TouchableOpacityScanAgain}
                onPress={() => 
                    this.setState({ scanned: false, tableId: null })
                }
            >
                <View
                    style={styles.ViewScanAgain}
                >
                        <Text
                            style={styles.TextScanAgain}
                        >
                            Scan Again
                        </Text>
                </View>

            </TouchableOpacity>
            )}

            {scanned && (<TouchableOpacity
                style={styles.TouchableOpacityConfirm}
                onPress={() => this.putTableId()}
            >
                <View
                    style={styles.ViewConfirm}
                >
                        <Text
                            style={styles.TextConfirm}
                        >
                            Confirm
                        </Text>
                </View>

            </TouchableOpacity>
            )}
        </View>)}

      </View>
    );
  }
}

export default Scan;
