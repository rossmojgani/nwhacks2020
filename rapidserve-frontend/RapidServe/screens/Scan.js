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
    }
});

class Scan extends React.Component {
    state = {
        hasCameraPermission: null,
        scanned: false,
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
        alert(`Table ID: ${data} has been scanned!`);
    };

    putTableId = ({userId, tableId}) => {
        fetch("http://34.83.193.124/" + userId, {
            method: "PUT",
            body: JSON.stringify({
                tableId
            })
        }).then((response) => {
            this.props.navigation.navigate("CustomerView", {
                tableId: response,
            })
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
          style={styles.Scanner}
        />

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
                onPress={() => this.setState({ scanned: false })}
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
                onPress={() => this.putTableId("12345", data)}
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
