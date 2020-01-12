import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
import Scan from "./screens/Scan"

export default function App() {
  return (
    <Scan/>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
});
