#include <time.h>
#include <assert.h>
#include <stdlib.h>
#include <stdio.h>
#include <errno.h>

// This function generates a random array of floats of length SIZE,
// within the real interval [-BOUND, BOUND]
int8_t* generate_random_list(const long int SIZE, const int BOUND){
  assert(SIZE > 0 && "Size must be positive");
  assert(BOUND > 0 && "Bound must be positive");
  // We need to allocate a new array because we need the array past the function call.
  int8_t* random_array = (int8_t*) malloc(SIZE*sizeof(int8_t));
  if (!random_array){
    perror("malloc failed");
    exit(-1);
  }
  int8_t random_number;
  for(int i = 0; i < SIZE; i++){
    random_number = ((int8_t)rand()/RAND_MAX*(2*BOUND)) - BOUND;
    random_array[i] = random_number;
  }
  return random_array;
}

// Update location by velocity, one time-step
void update_coords(int8_t* x, int8_t* y, int8_t* z, int8_t* vx, int8_t* vy, int8_t* vz, const long int SIZE){
  for(int i = 0; i < SIZE; i++){
    x[i] += vx[i];
    y[i] += vy[i];
    z[i] += vz[i];
  }
}


// Returns the average runtime for the update_coords function in microseconds
double timeit(int8_t* x, int8_t* y, int8_t* z, int8_t* vx, int8_t* vy, int8_t* vz, const long int SIZE, const long int ITERS){
  struct timespec start, end;
  double time = 0.0;
  clock_gettime(CLOCK_MONOTONIC, &start);
  
  for(int i = 0; i < ITERS; i++){
    update_coords(x, y, z, vx, vy, vz, SIZE);
    time += (end.tv_nsec - start.tv_nsec);
    
  }
  clock_gettime(CLOCK_MONOTONIC, &end);
  time = (end.tv_sec - start.tv_sec)*1000000.0; // conversion to microseconds
  time += (end.tv_nsec - start.tv_nsec)*0.001;
  return time/(ITERS*SIZE);
}

// Returns the sum of the elements in a list
int8_t sum(int8_t* list, const long int size){
  int8_t sum_total = 0;
  for(int i=0; i<size; i++){
    sum_total += list[i];
  }
  return sum_total;
}

int main(int argc, char* argv[]){
  if (argc != 3){
    printf("Required arguments: vector_length and iterations_num");
    return -1;
  }

  const long int SIZE = atoi(argv[1]);
  const long int ITERS = atoi(argv[2]);

  srand(SIZE);

  int8_t* x = generate_random_list(SIZE, 1000);
  int8_t* y = generate_random_list(SIZE, 1000);
  int8_t* z = generate_random_list(SIZE, 1000);
  int8_t* vx = generate_random_list(SIZE, 1);
  int8_t* vy = generate_random_list(SIZE, 1);
  int8_t* vz = generate_random_list(SIZE, 1);

  double average_time = timeit(x,y,z,vx,vy,vz, SIZE, ITERS);

  int8_t chksum = sum(x,SIZE) + sum(y, SIZE) + sum(z, SIZE);
  printf("Mean time per coordinate: %fus\n", average_time);
  printf("Final checksum is: %i\n", chksum);
  
  // free the memory from the dynamically-allocated arrays
  free(x);
  free(y);
  free(z);
  free(vx);
  free(vy);
  free(vz);
  
  return 0;
}
