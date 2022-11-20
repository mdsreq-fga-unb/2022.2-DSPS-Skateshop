import { BrowserRouter } from "react-router-dom";
import RoutesComponent from "./routes";
import GlobalStyle from "./styles/global";

function App(): JSX.Element {
  return (
    <BrowserRouter basename="/2022.2-DSPS-Skateshop/">
      <RoutesComponent />
      <GlobalStyle />
    </BrowserRouter>
  );
}

export default App;
