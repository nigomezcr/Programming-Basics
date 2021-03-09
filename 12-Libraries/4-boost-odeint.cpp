#include <iostream>
#include <vector>
#include <boost/numeric/odeint.hpp>

using namespace boost::numeric::odeint;
typedef std::vector<double> state_type;

//Define the system of ODE as a class
class harmonic_oscilator{
  double m_gamma;

public:
  harmonic_oscilator( double gamma ) : m_gamma (gamma) {}

  void operator()(const state_type &x, state_type & dxdt, const double t)
  {
    dxdt[0] = x[1];
    dxdt[1] = -x[0] - gamma*x[1];
  }

};

//To print the system, defin an observer
struct push_back_state_and_time{
  std::vector<state_type>& m_states;
  std::vector<state_type>& m_times;

  push_back_state_and_time( std::vector<state_type>  &states, std::vector<double> times)
  : m_states(states) , m_times(times) {}

  void operator()(const state_type &x, double t)
  {
    m_states.push_back(x);
    m_times.push_back(t);
  }
};


int main(void)
{
  std::vector<state_type> x_vec;
  std::vector<double> time;

  double t0 = 0, tf = 10, dt = 0.01;

  size_t steps = integrate( harmonic_oscilator,
                            x, t0, ti, dt,
                            push_back_state_and_time ( x_vec, time));

  for(size_t i = 0; i <= steps; i++)
  {
    std::cout  << time << '\t' << x_vec[i][0] << '\t' << x_vec[i][1] << std::endl;
  }

}
